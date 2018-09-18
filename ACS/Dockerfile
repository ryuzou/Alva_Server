FROM rails:4.2.5.1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      mysql-client \
      libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN gem install bundler \
  && bundle install --path vendor/bundle