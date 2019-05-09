# -*- coding: utf-8 -*-
import datetime

from metadata_tool import structure as s
from metadata_tool.dialects.oep.parser import JSONParser_1_4

from ..base.parser import _test_generic_parsing


def test_parser_v1_4():
    parser = JSONParser_1_4()
    _input_file = "tests/data/metadata_v14.json"
    expected_result = s.OEPMetadata(
        name="oep_metadata_table_example_v14",
        title="Good example title",
        identifier="http://openenergyplatform.org/dataedit/view/model_draft/oep_metadata_table_example_v14",
        description="example metadata for example data",
        languages=["en-GB", "en-US", "de-DE", "fr-FR"],
        keywords=["example", "template", "test"],
        publication_date=datetime.datetime(2018, 6, 12, 0, 0),
        context=s.Context(
            homepage="https://reiner-lemoine-institut.de/szenariendb/",
            documentation="https://github.com/OpenEnergyPlatform/organisation/wiki/metadata",
            source_code="https://github.com/OpenEnergyPlatform/examples/tree/master/metadata",
            contact="https://github.com/Ludee",
            grant_number="03ET4057",
        ),
        spatial=s.Spatial(location=None, extend="europe", resolution="100 m"),
        temporal=s.Temporal(
            reference_date=datetime.datetime(2016, 1, 1, 0, 0),
            start=datetime.datetime(
                2017, 1, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 3600))
            ),
            end=datetime.datetime(
                2017,
                12,
                31,
                23,
                0,
                tzinfo=datetime.timezone(datetime.timedelta(0, 3600)),
            ),
            resolution="1 h",
            ts_orientation=s.TimestampOrientation.left
        ),
        sources=[
            s.Source(
                title="OpenEnergyPlatform Metadata Example",
                description="Metadata description",
                path="https://github.com/OpenEnergyPlatform",
                source_license=s.License(
                    None,
                    "Creative Commons Zero v1.0 Universal (CC0-1.0)",
                    None,
                    None,
                    None,
                ),
                source_copyright="© Reiner Lemoine Institut",
            ),
            s.Source(
                title="OpenStreetMap",
                description="A collaborative project to create a free editable map of the world",
                path="https://www.openstreetmap.org/",
                source_license=s.License(None, "ODbL-1.0", None, None, None),
                source_copyright="© OpenStreetMap contributors",
            ),
        ],
        object_licenses=[
            s.License(
                name="ODbL-1.0",
                title="Open Data Commons Open Database License 1.0",
                path="https://opendatacommons.org/licenses/odbl/1.0/",
                instruction="You are free: To Share, To Create, To Adapt; As long as you: Attribute, Share-Alike, Keep open!",
                attribution="© Reiner Lemoine Institut",
            )
        ],
        contributors=[
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2016,6,16),
                obj="metadata",
                comment="Create metadata",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2016,11,22),
                obj="metadata",
                comment="Update metadata",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2016,11,22),
                obj="metadata",
                comment="Update header and license",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2017,3,16),
                obj="metadata",
                comment="Add license to source",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2017,3,28),
                obj="metadata",
                comment="Add copyright to source and license",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2017,5,30),
                obj="metadata",
                comment="Release metadata version 1.3",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2017,6,26),
                obj="metadata",
                comment="Move referenceDate into temporal and remove array",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2018,7,19),
                obj="metadata",
                comment="Start metadata version 1.4",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2018,7,26),
                obj="data",
                comment="Rename table and files",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2018,10,18),
                obj="metadata",
                comment="Add contribution object",
            ),
            s.Contributor(
                title="christian-rli",
                email=None,
                date=datetime.date(2018,10,18),
                obj="metadata",
                comment="Add datapackage compatibility",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2018,11,2),
                obj="metadata",
                comment="Release metadata version 1.4",
            ),
            s.Contributor(
                title="christian-rli",
                email=None,
                date=datetime.date(2019,2,5),
                obj="metadata",
                comment="Apply template structure to example.",
            ),
            s.Contributor(
                title="Ludee",
                email=None,
                date=datetime.date(2019,3,22),
                obj="metadata",
                comment="Hotfix foreignKeys",
            ),
        ],
        resources=[
            s.Resource(
                name="model_draft.oep_metadata_table_example_v14",
                path="http://openenergyplatform.org/dataedit/view/model_draft/oep_metadata_table_example_v14",
                profile="tabular-data-resource",
                resource_format="PostgreSQL",
                encoding="UTF-8",
                schema=s.Schema(
                    fields=[
                        s.Field(
                            name="id",
                            description="Unique identifier",
                            field_type="serial",
                            unit=None,
                        ),
                        s.Field(
                            name="year",
                            description="Reference year",
                            field_type="integer",
                            unit=None,
                        ),
                        s.Field(
                            name="value",
                            description="Example value",
                            field_type="double precision",
                            unit="MW",
                        ),
                        s.Field(
                            name="geom",
                            description="Geometry",
                            field_type="geometry(Point, 4326)",
                            unit=None,
                        ),
                    ],
                    primary_key=["id"],
                    foreign_keys=[
                        s.ForeignKey(
                            fields=["year"],
                            reference=s.Reference(
                                resource="schema.table", fields=["year"]
                            ),
                        )
                    ],
                ),
            )
        ],
        review=s.Review(
            path="https://github.com/OpenEnergyPlatform/data-preprocessing/wiki",
            badge="platin",
        ),
        comment=s.MetaComment(
            metadata_info="Metadata documentation and explanation (https://github.com/OpenEnergyPlatform/organisation/wiki/metadata)",
            dates="Dates and time must follow the ISO8601 including time zone (YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh)",
            units="Use a space between numbers and units (100 m)",
            languages="Languages must follow the IETF (BCP47) format (en-GB, en-US, de-DE)",
            licenses="License name must follow the SPDX License List (https://spdx.org/licenses/)",
            review="Following the OEP Data Review (https://github.com/OpenEnergyPlatform/data-preprocessing/wiki)",
            none="If not applicable use (none)",
        ),
    )
    _test_generic_parsing(parser, _input_file, expected_result)