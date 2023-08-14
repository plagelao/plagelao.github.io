require 'yaml'

namespace :tags do
  task :populate do
    Dir["_posts/**/*.md"].each do |file|
      tag_line = File.readlines(file).detect do |line|
        line =~ /tags:/
      end
      YAML.load(tag_line)['tags'].each do |tag|
        if Dir["tags/**/*.md"].none?{|tag_file| tag_file.split('/').last.split('.').first == tag.downcase}
          content = ['---', 'layout: tag', "title: 'Tag: #{tag}'", "tag: #{tag}", '---'].join("\n")
          puts tag
          puts content
          File.write("tags/#{tag.downcase}.md", content)
        end
      end
    end
  end
end
