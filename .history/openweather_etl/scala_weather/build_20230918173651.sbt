name := "WeatherStreamingDemo"
version := "1.0"
scalaVersion := "2.12.10"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % "3.0.3",
  "org.apache.spark" %% "spark-streaming" % "3.0.3",
  "org.apache.spark" %% "spark-streaming-kafka-0-10" % "3.0.3",
  "org.apache.spark" %% "spark-sql-kafka-0-10" % "2.4.0",
  "org.apache.kafka" % "kafka-clients" % "1.1.0"
)