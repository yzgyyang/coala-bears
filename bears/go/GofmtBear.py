from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.AnyOneOfRequirements import (
    AnyOneOfRequirements)
from dependency_management.requirements.ExecutableRequirement import (
    ExecutableRequirement)
from dependency_management.requirements.DistributionRequirement import (
    DistributionRequirement)


@linter(executable='gofmt',
        use_stdin=True,
        output_format='corrected',
        result_message='Formatting can be improved.')
class GofmtBear:
    """
    Suggest better formatting options in Go code. Basic checks like alignment,
    indentation, and redundant parentheses are provided.

    This is done using the ``gofmt`` utility. For more information visit
    <https://golang.org/cmd/gofmt/>.
    """
    LANGUAGES = {'Go'}
    REQUIREMENTS = {
        AnyOneOfRequirements([
            DistributionRequirement('go'),
            ExecutableRequirement('gofmt'),
        ])
    }
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_FIX = {'Formatting', 'Code Simplification'}
    ASCIINEMA_URL = 'https://asciinema.org/a/94812'

    @staticmethod
    def create_arguments(filename, file, config_file,
                         simplify: bool = False,
                         ):
        """
        :param simplify: Tries to simplify code
        """
        args = ()
        if simplify:
            args += ('-s',)
        return args

    @classmethod
    def setup_dependencies(cls):
        for dep in cls.REQUIREMENTS:
            dep.install_all()
