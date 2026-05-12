source 'https://rubygems.org'

group :jekyll_plugins do
  gem 'jekyll', '~> 4.3'
  gem 'jekyll-feed'
  gem 'jekyll-sitemap'
  gem 'jekyll-redirect-from'
  gem 'jekyll-gist'
  gem 'jekyll-paginate'
  gem 'jemoji'
  gem 'webrick', '~> 1.8'
end

# Note: github-pages gem pins liquid 4.0.3 which calls String#tainted? (removed in Ruby 3.2+).
# For local preview only we use modern Jekyll directly. GitHub Pages still renders remotely on push.
gem 'connection_pool', '2.5.0'

# Ruby 3.4+ moved these out of the default gemset.
gem 'csv'
gem 'base64'
gem 'logger'
gem 'bigdecimal'
