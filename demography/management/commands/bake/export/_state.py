from geography.models import Division


class ExportState(object):
    def export_states(self, states):
        # TODO: Call export_data to export data for each state
        for fips in states:
            state = Division.objects.get(level=self.STATE_LEVEL, code=fips)
            print('>> Exporting: {}'.format(state.code))
            # state_data = self.aggregate_state_estimates_by_county(state)
            # self.export_state_files(bucket, state, state_data)
            # self.aggregate_state_estimates_by_district(state)
