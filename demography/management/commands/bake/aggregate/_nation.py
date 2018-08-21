from demography.models import CensusEstimate
from geography.models import Division


class AggregateNation(object):
    def aggregate_national_estimates_by_state(self):
        """
        Aggregates state-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/states.json
        """
        data = {}
        fips = '00'
        aggregated_labels = []
        states = Division.objects.filter(level=self.STATE_LEVEL)
        estimates = CensusEstimate.objects.filter(
            division__level=self.STATE_LEVEL)
        for estimate in estimates:
            series = estimate.variable.table.series
            year = estimate.variable.table.year
            table = estimate.variable.table.code
            label = estimate.variable.label.label
            table_label = '{}{}'.format(table, label)
            code = estimate.variable.code
            if series not in data:
                data[series] = {}
            if year not in data[series]:
                data[series][year] = {}
            if table not in data[series][year]:
                data[series][year][table] = {}
            if fips not in data[series][year][table]:
                data[series][year][table][fips] = {}
            if label is not None:
                if table_label not in aggregated_labels:
                    aggregated_labels.append(table_label)
                    data[series][year][table][fips][label] \
                        = [
                            self.aggregate_variable(estimate, division.id)
                            for division in states
                            if len(CensusEstimate.objects.filter(
                                variable=estimate.variable,
                                division=division.id)
                            ) > 0
                        ]
            else:
                if code in data[series][year][table][fips]:
                    data[series][year][table][fips][code].append(
                        estimate.estimate)
                else:
                    data[series][year][table][fips][code] \
                        = [estimate.estimate]
        # print(data)
        return data

    def aggregate_national_estimates_by_district(self):
        """
        Aggregates district-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/districts.json
        """
        data = {}
        fips = '00'
        aggregated_labels = []
        states = Division.objects.filter(level=self.DISTRICT_LEVEL)
        estimates = CensusEstimate.objects.filter(
            division__level=self.DISTRICT_LEVEL)
        for estimate in estimates:
            series = estimate.variable.table.series
            year = estimate.variable.table.year
            table = estimate.variable.table.code
            label = estimate.variable.label.label
            table_label = '{}{}'.format(table, label)
            code = estimate.variable.code
            if series not in data:
                data[series] = {}
            if year not in data[series]:
                data[series][year] = {}
            if table not in data[series][year]:
                data[series][year][table] = {}
            if fips not in data[series][year][table]:
                data[series][year][table][fips] = {}
            if label is not None:
                if table_label not in aggregated_labels:
                    # c= {**a, **b}
                    aggregated_labels.append(table_label)
                    data[series][year][table][fips][label] \
                        = [
                            self.aggregate_variable(estimate, division.id)
                            for division in states
                            if len(CensusEstimate.objects.filter(
                                variable=estimate.variable,
                                division=division.id)
                            ) > 0
                        ]
            else:
                if code in data[series][year][table][fips]:
                    data[series][year][table][fips][code].append(
                        estimate.estimate)
                else:
                    data[series][year][table][fips][code] \
                        = [estimate.estimate]
        # print(data)
        return data
