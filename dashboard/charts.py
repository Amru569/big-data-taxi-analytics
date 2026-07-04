import plotly.express as px


class DashboardCharts:

    @staticmethod
    def peak_hour_chart(df):

        fig = px.bar(

            df,

            x="pickup_hour",

            y="Total Trips",

            title="Trips by Pickup Hour"

        )

        return fig

    @staticmethod
    def payment_chart(df):

        fig = px.pie(

            df,

            names="payment_type",

            values="Trips",

            title="Payment Distribution"

        )

        return fig

    @staticmethod
    def pickup_chart(df):

        fig = px.bar(

            df,

            x="Pickup_Zone",

            y="Trips",

            title="Top Pickup Zones"

        )

        return fig

    @staticmethod
    def dropoff_chart(df):

        fig = px.bar(

            df,

            x="Dropoff_Zone",

            y="Trips",

            title="Top Dropoff Zones"

        )

        return fig