---
title: repository_advisories
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_advisories
  - security_advisories
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_advisories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.security_advisories.repository_advisories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A detailed description of what the advisory entails. |
| <CopyableCode code="author" /> | `null` | The author of the advisory. |
| <CopyableCode code="closed_at" /> | `string` | The date and time of when the advisory was closed, in ISO 8601 format. |
| <CopyableCode code="collaborating_teams" /> | `array` | A list of teams that collaborate on the advisory. |
| <CopyableCode code="collaborating_users" /> | `array` | A list of users that collaborate on the advisory. |
| <CopyableCode code="created_at" /> | `string` | The date and time of when the advisory was created, in ISO 8601 format. |
| <CopyableCode code="credits" /> | `array` |  |
| <CopyableCode code="credits_detailed" /> | `array` |  |
| <CopyableCode code="cve_id" /> | `string` | The Common Vulnerabilities and Exposures (CVE) ID. |
| <CopyableCode code="cvss" /> | `object` |  |
| <CopyableCode code="cwe_ids" /> | `array` | A list of only the CWE IDs. |
| <CopyableCode code="cwes" /> | `array` |  |
| <CopyableCode code="ghsa_id" /> | `string` | The GitHub Security Advisory ID. |
| <CopyableCode code="html_url" /> | `string` | The URL for the advisory. |
| <CopyableCode code="identifiers" /> | `array` |  |
| <CopyableCode code="private_fork" /> | `null` | A temporary private fork of the advisory's repository for collaborating on a fix. |
| <CopyableCode code="published_at" /> | `string` | The date and time of when the advisory was published, in ISO 8601 format. |
| <CopyableCode code="publisher" /> | `null` | The publisher of the advisory. |
| <CopyableCode code="severity" /> | `string` | The severity of the advisory. |
| <CopyableCode code="state" /> | `string` | The state of the advisory. |
| <CopyableCode code="submission" /> | `object` |  |
| <CopyableCode code="summary" /> | `string` | A short summary of the advisory. |
| <CopyableCode code="updated_at" /> | `string` | The date and time of when the advisory was last updated, in ISO 8601 format. |
| <CopyableCode code="url" /> | `string` | The API URL for the advisory. |
| <CopyableCode code="vulnerabilities" /> | `array` |  |
| <CopyableCode code="withdrawn_at" /> | `string` | The date and time of when the advisory was withdrawn, in ISO 8601 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_repository_advisory" /> | `SELECT` | <CopyableCode code="ghsa_id, owner, repo" /> | Get a repository security advisory using its GitHub Security Advisory (GHSA) identifier.<br />You can access any published security advisory on a public repository.<br />You must authenticate using an access token with the `repo` scope or `repository_advisories:read` permission<br />in order to get a published security advisory in a private repository, or any unpublished security advisory that you have access to.<br /><br />You can access an unpublished security advisory from a repository if you are a security manager or administrator of that repository, or if you are a<br />collaborator on the security advisory. |
| <CopyableCode code="list_org_repository_advisories" /> | `SELECT` | <CopyableCode code="org" /> | Lists repository security advisories for an organization.<br /><br />To use this endpoint, you must be an owner or security manager for the organization, and you must use an access token with the `repo` scope or `repository_advisories:write` permission. |
| <CopyableCode code="list_repository_advisories" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists security advisories in a repository.<br />You must authenticate using an access token with the `repo` scope or `repository_advisories:read` permission<br />in order to get published security advisories in a private repository, or any unpublished security advisories that you have access to.<br /><br />You can access unpublished security advisories from a repository if you are a security manager or administrator of that repository, or if you are a collaborator on any security advisory. |
| <CopyableCode code="create_repository_advisory" /> | `INSERT` | <CopyableCode code="owner, repo, data__description, data__summary, data__vulnerabilities" /> | Creates a new repository security advisory.<br />You must authenticate using an access token with the `repo` scope or `repository_advisories:write` permission to use this endpoint.<br /><br />In order to create a draft repository security advisory, you must be a security manager or administrator of that repository. |
| <CopyableCode code="create_private_vulnerability_report" /> | `EXEC` | <CopyableCode code="owner, repo, data__description, data__summary" /> | Report a security vulnerability to the maintainers of the repository.<br />See "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)" for more information about private vulnerability reporting. |
| <CopyableCode code="create_repository_advisory_cve_request" /> | `EXEC` | <CopyableCode code="ghsa_id, owner, repo" /> | If you want a CVE identification number for the security vulnerability in your project, and don't already have one, you can request a CVE identification number from GitHub. For more information see "[Requesting a CVE identification number](https://docs.github.com/code-security/security-advisories/repository-security-advisories/publishing-a-repository-security-advisory#requesting-a-cve-identification-number-optional)."<br /><br />You may request a CVE for public repositories, but cannot do so for private repositories.<br /><br />You must authenticate using an access token with the `repo` scope or `repository_advisories:write` permission to use this endpoint.<br /><br />In order to request a CVE for a repository security advisory, you must be a security manager or administrator of that repository. |
| <CopyableCode code="update_repository_advisory" /> | `EXEC` | <CopyableCode code="ghsa_id, owner, repo" /> | Update a repository security advisory using its GitHub Security Advisory (GHSA) identifier.<br />You must authenticate using an access token with the `repo` scope or `repository_advisories:write` permission to use this endpoint.<br /><br />In order to update any security advisory, you must be a security manager or administrator of that repository,<br />or a collaborator on the repository security advisory. |
