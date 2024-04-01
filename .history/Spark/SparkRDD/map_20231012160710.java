package demo;

import java.util.Arrays;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;

public class map {
	public static void main(String[] args) {
		SparkConf conf = new SparkConf()
				.setAppName("Demo")
				.setMaster("local[2]");
		
		try (JavaSparkContext sc = new JavaSparkContext(conf)) {
			List<Integer> list = Arrays.asList(10,20,30);
			JavaRDD<Integer> data = sc.parallelize(list);
			
			data = data.map(new Function<Integer, Integer>() {
				private static final long serialVersionUID = 1L;

				@Override
				public Integer call(Integer v1) throws Exception {
					return v1 * 2;
				}
				
			});
			
			data.collect().forEach(v -> System.out.println(v));
		}
		
	}
}