name := "WeatherStreamingDemo"
version := "1.0"
scalaVersion := "2.13.8"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % "3.0.2", // Use an alternative version (e.g., 3.0.2)
  "org.apache.spark" %% "spark-streaming" % "3.0.2", // Use an alternative version (e.g., 3.0.2)
  "org.apache.spark" %% "spark-streaming-kafka-0-10" % "3.0.2", // Use an alternative version (e.g., 3.0.2)
  "org.apache.spark" %% "spark-sql-kafka-0-10" % "2.4.7", // Use an alternative version (e.g., 2.4.7)
  "org.apache.kafka" % "kafka-clients" % "2.8.0" // Use an alternative version (e.g., 2.8.0)
)
