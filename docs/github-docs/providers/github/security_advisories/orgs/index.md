---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.security_advisories.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A detailed description of what the advisory entails. |
| `publisher` | `null` | The publisher of the advisory. |
| `author` | `null` | The author of the advisory. |
| `credits` | `array` |  |
| `published_at` | `string` | The date and time of when the advisory was published, in ISO 8601 format. |
| `summary` | `string` | A short summary of the advisory. |
| `cwe_ids` | `array` | A list of only the CWE IDs. |
| `cvss` | `object` |  |
| `cwes` | `array` |  |
| `updated_at` | `string` | The date and time of when the advisory was last updated, in ISO 8601 format. |
| `closed_at` | `string` | The date and time of when the advisory was closed, in ISO 8601 format. |
| `private_fork` | `null` | A temporary private fork of the advisory's repository for collaborating on a fix. |
| `url` | `string` | The API URL for the advisory. |
| `credits_detailed` | `array` |  |
| `cve_id` | `string` | The Common Vulnerabilities and Exposures (CVE) ID. |
| `vulnerabilities` | `array` |  |
| `state` | `string` | The state of the advisory. |
| `ghsa_id` | `string` | The GitHub Security Advisory ID. |
| `collaborating_teams` | `array` | A list of teams that collaborate on the advisory. |
| `withdrawn_at` | `string` | The date and time of when the advisory was withdrawn, in ISO 8601 format. |
| `collaborating_users` | `array` | A list of users that collaborate on the advisory. |
| `severity` | `string` | The severity of the advisory. |
| `submission` | `object` |  |
| `identifiers` | `array` |  |
| `created_at` | `string` | The date and time of when the advisory was created, in ISO 8601 format. |
| `html_url` | `string` | The URL for the advisory. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_org_repository_advisories` | `SELECT` | `org` |
