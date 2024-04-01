package groupbykey;

import java.util.Arrays;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;

public class groupbyKey {
	public static void main(String[] args) {
		SparkConf conf = new SparkConf()
				.setAppName("Demo")
				.setMaster("local[2]");
	
		try (JavaSparkContext sc = new JavaSparkContext(conf)) {
			List<Tuple2<String, Integer>> list = Arrays.asList(
					new Tuple2<String, Integer>("C", 3), 
					new Tuple2<String, Integer>("A", 1), 
					new Tuple2<String, Integer>("B", 4), 
					new Tuple2<String, Integer>("A", 2), 
					new Tuple2<String, Integer>("B", 5));
			
			JavaPairRDD<String, Integer> data = sc.parallelizePairs(list);
			data.groupByKey().collect().forEach(s -> System.out.println(s));
			
		}
	}
}