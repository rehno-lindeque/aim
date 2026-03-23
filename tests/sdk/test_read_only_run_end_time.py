from aim.sdk.run import Run
from tests.base import TestBase


class TestReadOnlyRunEndTime(TestBase):
    def test_read_only_run_sees_end_time_after_close(self):
        run = Run(system_tracking_interval=None)
        run.track(1.23, name='loss', step=1)
        run.report_successful_finish()
        run.close()

        rehydrated = Run(run.hash, repo=self.repo.path, read_only=True, system_tracking_interval=None)

        self.assertIsNotNone(rehydrated.end_time)
        self.assertIsNotNone(rehydrated.finalized_at)
