name := "WeatherStreamingDemo"
version := "1.0"
scalaVersion := "2.13.8"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % "3.1.2",
  "org.apache.spark" %% "spark-streaming" % "3.1.2",
  "org.apache.spark" %% "spark-streaming-kafka-0-10" % "3.1.2",
  // Add other dependencies as needed
)