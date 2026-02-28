from metaflow import FlowSpec, step
class TabTest(FlowSpec):
    @step
    def start(self):
        self.secret_artifact = "found me!"
        self.next(self.end)
    @step
    def end(self):
        pass
if __name__ == '__main__':
    TabTest()