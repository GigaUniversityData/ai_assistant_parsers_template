from .level_0 import (
    ApmathDomainParser,
)
from .level_1 import (
    FakultetApmathDomainParser,
    N14PrepodavateliApmathDomainParser,
    N16FacultyApmathDomainParser,
    StudentamApmathDomainParser,
)
from .level_2 import (
    Fakultet14PrepodavateliApmathDomainParser,
    FakultetKafedryApmathDomainParser,
    FakultetOtdelyIKomissiiApmathDomainParser,
    FakultetPrepodavateliApmathDomainParser,
    RuFakuletApmathDomainParser,
)
from .level_3 import (
    FakultetDekan16FacultyApmathDomainParser,
    FakultetKafedry2UncategorisedApmathDomainParser,
    FakultetSpisokIRejtingNauchnoPedagogicheskikhRabotnikov14PrepodavateliApmathDomainParser,
    FakultetSpisokIRejtingNauchnoPedagogicheskikhRabotnikov16FacultyApmathDomainParser,
    RuFakuletPrepodavateliApmathDomainParser,
    StudentamSpisokIRejtingPrepodavatelej14PrepodavateliApmathDomainParser,
    StudentamSpisokIRejtingPrepodavatelej16FacultyApmathDomainParser,
)
from .level_4 import (
    FakultetOtdelyIKomissiiUchebnyjOtdel17DepartmentsAndCommissionsApmathDomainParser,
)

__all__ = [
    "ApmathDomainParser",
    "Fakultet14PrepodavateliApmathDomainParser",
    "FakultetApmathDomainParser",
    "FakultetDekan16FacultyApmathDomainParser",
    "FakultetKafedry2UncategorisedApmathDomainParser",
    "FakultetKafedryApmathDomainParser",
    "FakultetOtdelyIKomissiiApmathDomainParser",
    "FakultetOtdelyIKomissiiUchebnyjOtdel17DepartmentsAndCommissionsApmathDomainParser",
    "FakultetPrepodavateliApmathDomainParser",
    "FakultetSpisokIRejtingNauchnoPedagogicheskikhRabotnikov14PrepodavateliApmathDomainParser",
    "FakultetSpisokIRejtingNauchnoPedagogicheskikhRabotnikov16FacultyApmathDomainParser",
    "N14PrepodavateliApmathDomainParser",
    "N16FacultyApmathDomainParser",
    "RuFakuletApmathDomainParser",
    "RuFakuletPrepodavateliApmathDomainParser",
    "StudentamApmathDomainParser",
    "StudentamSpisokIRejtingPrepodavatelej14PrepodavateliApmathDomainParser",
    "StudentamSpisokIRejtingPrepodavatelej16FacultyApmathDomainParser",
]
