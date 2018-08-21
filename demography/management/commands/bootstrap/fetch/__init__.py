from tqdm import tqdm

from demography.models import CensusTable

from ._county import GetCounty
from ._district import GetDistrict
from ._series import GetSeries
from ._state import GetState


class Fetcher(GetCounty, GetDistrict, GetSeries, GetState):
    def fetch_census_data(self, states):
        """
        Fetch census estimates from table.
        """
        print('Fetching census data')
        for table in CensusTable.objects.all():
            api = self.get_series(table.series)
            for variable in table.variables.all():
                estimate = '{}_{}'.format(
                    table.code,
                    variable.code
                )
                print('>> Fetching {} {} {}'.format(
                    table.year,
                    table.series,
                    estimate
                ))
                for state in tqdm(states):
                    self.get_state_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )
                    self.get_county_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )
                    self.get_district_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )
