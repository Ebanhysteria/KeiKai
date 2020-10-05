const config = {
  gatsby: {
    pathPrefix: '/',
    siteUrl: 'http://keikai-map.s3-website-us-east-1.amazonaws.com/',
    gaTrackingId: null,
    trailingSlash: false,
  },
  header: {
    logo: '',
    logoLink: 'http://keikai-map.s3-website-us-east-1.amazonaws.com/',
    title:
      "",
    githubUrl: 'https://github.com/KeiKai',
    helpUrl: '',
    tweetText: '',
    social: `<li>
		    <a href="https://twitter.com/keikai" target="_blank" rel="noopener">
		      <div class="twitterBtn">
		        <img src='https://graphql-engine-cdn.hasura.io/learn-hasura/assets/homepage/twitter-brands-block.svg' alt={'Twitter'}/>
		      </div>
		    </a>
		  </li>
			<li>
		    <a href="https://discordapp.com/invite/keikai" target="_blank" rel="noopener">
		      <div class="discordBtn">
		        <img src='https://graphql-engine-cdn.hasura.io/learn-hasura/assets/homepage/discord-brands-block.svg' alt={'Discord'}/>
		      </div>
		    </a>
		  </li>`,
    links: [{ text: '', link: '' }],
    search: {
      enabled: false,
      indexName: '',
      algoliaAppId: process.env.GATSBY_ALGOLIA_APP_ID,
      algoliaSearchKey: process.env.GATSBY_ALGOLIA_SEARCH_KEY,
      algoliaAdminKey: process.env.ALGOLIA_ADMIN_KEY,
    },
  },
  sidebar: {
    forcedNavOrder: [
      // '/about project',
      '/project development'
    ],
    collapsedNav: [
      '/about project',
      // '/project development', // add trailing slash if enabled above
    ],
    links: [{ text: 'Keikai', link: 'http://keikai-map.s3-website-us-east-1.amazonaws.com/' }],
    frontline: false,
    ignoreIndex: true,
    title:
      "<a href='http://keikai-map.s3-website-us-east-1.amazonaws.com/'>Keikai </a><div class='greenCircle'></div><a href='https://www.spaceappschallenge.org/'>NASA</a>",
  },
  siteMetadata: {
    title: 'Keikai',
    description: '',
    ogImage: null,
    docsLocation: 'https://github.com/KeiKai',
    favicon: 'https://keikai-documentation.s3.amazonaws.com/pwa-512.svg',
  },
  pwa: {
    enabled: false, // disabling this will also remove the existing service worker.
    manifest: {
      name: 'Gatsby Gitbook Starter',
      short_name: 'GitbookStarter',
      start_url: '/',
      background_color: '#6b37bf',
      theme_color: '#6b37bf',
      display: 'standalone',
      crossOrigin: 'use-credentials',
      icons: [
        {
          src: '',
          sizes: `512x512`,
          type: `image/png`,
        },
      ],
    },
  },
};

module.exports = config;
