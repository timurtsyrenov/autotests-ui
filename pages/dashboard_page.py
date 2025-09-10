from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
