import os
import json
from demography.conf import settings

from ._aws import get_bucket

OUTPUT_PATH = os.path.join(
    settings.AWS_S3_UPLOAD_ROOT,
    'data/us-census'
)


class ExportData(object):
    @staticmethod
    def export_data(division, subdivision_level, data):
        bucket = get_bucket()

        for series in data.keys():
            for year in data[series].keys():
                for table in data[series][year].keys():
                    key = os.path.join(
                        OUTPUT_PATH,
                        series,
                        year,
                        table,
                        division.code,
                        '{}.json'.format(subdivision_level)
                    )
                    bucket.put_object(
                        Key=key,
                        ACL=settings.AWS_ACL,
                        Body=json.dumps(data[series][year][table]),
                        CacheControl=settings.AWS_CACHE_HEADER,
                        ContentType='application/json'
                    )
