from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        self.execute(r"C:\Users\jasantos\Fakturama2\Fakturama.exe")
        # Fetch the Activity ID from the task:
        task = self.maestro.get_task(execution.task_id)
        activity_id = task.activity_id

        # Opens the BotCity website.
        # self.browse("http://www.botcity.dev")

        # Uncomment to mark this task as finished on BotMaestro
        self.maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK."
        )
        if not self.find("new_product_btn", matching=0.97, waiting_time=10000):
            self.not_found("new_product_btn")
        self.click()

        if not self.find("Item_number", matching=0.97, waiting_time=10000):
            self.not_found("Item_number")
        self.click_relative(95, 5)

        self.paste("1")
        self.tab()
        self.paste("Primeiro produto")
        self.tab()
        self.paste("Categoria 1")
        self.tab()
        self.paste("12345")
        self.tab()
        self.paste("99")
        self.tab()
        self.paste("Isso é um teste de inserção")
        self.tab()
        self.control_a()
        self.paste("10,99")
        self.enter()
        self.control_a()
        self.paste("2,99")
        self.enter()
        self.control_a()
        self.paste("20")
        self.enter()
        self.tab
        if not self.find("Stock", matching=0.97, waiting_time=10000):
            self.not_found("Stock")
        self.click_relative(46, 6)
        self.control_a()
        self.paste("10")
        if not self.find("Select_picture", matching=0.97, waiting_time=10000):
            self.not_found("Select_picture")
        self.click()
        self.wait(500)
        self.click()
        self.paste(
            r"C:\Users\jasantos\Documents\Projeto\BotCity\ProjFakturama\icone.png")
        self.enter()
        if not self.find("Save_btn", matching=0.97, waiting_time=10000):
            self.not_found("Save_btn")
        self.click()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
