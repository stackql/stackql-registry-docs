---
title: global_advisories
hide_title: false
hide_table_of_contents: false
keywords:
  - global_advisories
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
<tr><td><b>Name</b></td><td><code>global_advisories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.security_advisories.global_advisories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A detailed description of what the advisory entails. |
| <CopyableCode code="credits" /> | `array` | The users who contributed to the advisory. |
| <CopyableCode code="cve_id" /> | `string` | The Common Vulnerabilities and Exposures (CVE) ID. |
| <CopyableCode code="cvss" /> | `object` |  |
| <CopyableCode code="cwes" /> | `array` |  |
| <CopyableCode code="ghsa_id" /> | `string` | The GitHub Security Advisory ID. |
| <CopyableCode code="github_reviewed_at" /> | `string` | The date and time of when the advisory was reviewed by GitHub, in ISO 8601 format. |
| <CopyableCode code="html_url" /> | `string` | The URL for the advisory. |
| <CopyableCode code="identifiers" /> | `array` |  |
| <CopyableCode code="nvd_published_at" /> | `string` | The date and time when the advisory was published in the National Vulnerability Database, in ISO 8601 format.<br />This field is only populated when the advisory is imported from the National Vulnerability Database. |
| <CopyableCode code="published_at" /> | `string` | The date and time of when the advisory was published, in ISO 8601 format. |
| <CopyableCode code="references" /> | `array` |  |
| <CopyableCode code="repository_advisory_url" /> | `string` | The API URL for the repository advisory. |
| <CopyableCode code="severity" /> | `string` | The severity of the advisory. |
| <CopyableCode code="source_code_location" /> | `string` | The URL of the advisory's source code. |
| <CopyableCode code="summary" /> | `string` | A short summary of the advisory. |
| <CopyableCode code="type" /> | `string` | The type of advisory. |
| <CopyableCode code="updated_at" /> | `string` | The date and time of when the advisory was last updated, in ISO 8601 format. |
| <CopyableCode code="url" /> | `string` | The API URL for the advisory. |
| <CopyableCode code="vulnerabilities" /> | `array` | The products and respective version ranges affected by the advisory. |
| <CopyableCode code="withdrawn_at" /> | `string` | The date and time of when the advisory was withdrawn, in ISO 8601 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_global_advisory" /> | `SELECT` | <CopyableCode code="ghsa_id" /> | Gets a global security advisory using its GitHub Security Advisory (GHSA) identifier. |
| <CopyableCode code="list_global_advisories" /> | `SELECT` |  | Lists all global security advisories that match the specified parameters. If no other parameters are defined, the request will return only GitHub-reviewed advisories that are not malware.<br /><br />By default, all responses will exclude advisories for malware, because malware are not standard vulnerabilities. To list advisories for malware, you must include the `type` parameter in your request, with the value `malware`. For more information about the different types of security advisories, see "[About the GitHub Advisory database](https://docs.github.com/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database#about-types-of-security-advisories)." |
