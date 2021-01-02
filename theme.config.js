export default {
  repository: 'https://github.com/zhqu1148980644/leetcode', // project repo
  docsRepository: 'https://github.com/zhqu1148980644/leetcode', // docs repo
  branch: 'master', // branch of docs
  path: '/', // path of docs
  titleSuffix: ' - leetcode',
  nextLinks: true,
  prevLinks: true,
  search: true,
  customSearch: null, // customizable, you can use algolia for example
  darkMode: true,
  footer: true,
  footerText: <>MIT {new Date().getFullYear()} © bakezq</>,
  footerEditOnGitHubLink: true, // will link to the docs repo
  logo: <>
    <svg>...</svg>
    <span>leetcode solutions</span>
  </>,
  head: <>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="leetcode solutions" />
    <meta name="og:title" content="leetcode solutions" />
  </>
}

