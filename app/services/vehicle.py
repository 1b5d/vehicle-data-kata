import csv
from app.exceptions import DataReadingError, FormatNotSupportedError


class BaseParser(object):
    """
    A general base parser for vehicle data.
    """
    def iter_data(self, content):
        """
        iterate over the parsed data.

        :param str content:
        :return iterator:
        """
        raise NotImplementedError()


class VehicleDataParser(BaseParser):
    """
    A wrapper of the content parser.
    """
    def parse_iter(self, content):
        """
        parses the content and iterates over the results.

        :param str content:
        :return iterator:
        """
        yield from super().iter_data(content)


class CSVParser(BaseParser):
    """
    Parser for the CSV data format.
    """
    def iter_data(self, content):
        """
        :param str content:
        :return iterator:
        """
        reader = csv.reader(content.split())
        try:
            for line in reader:
                yield {'vin': line[0],
                       'data1': line[1],
                       'data2': line[2],
                       'make': line[3]}
        except (KeyError, IndexError) as e:
            raise DataReadingError('Error reading data, inner exception: {exp}'.format(
                exp=str(e)))


class CSVVehicleDataParser(VehicleDataParser, CSVParser):
    pass


class HandlerService(object):
    """
    Represents the handler framework.
    """
    handler_mapping = {}

    @classmethod
    def register(cls, name, handler_class):
        """
        Registers a handler for a specific format.

        :param str name:
        :param type handler_class:
        :return:
        """
        cls.handler_mapping[name] = handler_class

    @classmethod
    def dispatch(cls, name):
        """
        Initiates a handler object based on a format.

        :param str name:
        :return VehicleDataParser:
        """
        handler_class = cls.handler_mapping.get(name)
        if not handler_class:
            raise FormatNotSupportedError(
                'Format {name} is not supported'.format(name=name))
        return handler_class()


HandlerService.register('csv', CSVVehicleDataParser)
