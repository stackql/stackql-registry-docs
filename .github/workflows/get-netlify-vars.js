module.exports = async ({ github, context, core, pathOutput }) => {
console.log('context is %o', context)
const workspace = process.env.GITHUB_WORKSPACE
const contents = readFileSync(`${workspace}/providers.txt`, 'utf-8');
console.log('contents are %o', contents)
const arr = contents.split(/\r?\n/);

}