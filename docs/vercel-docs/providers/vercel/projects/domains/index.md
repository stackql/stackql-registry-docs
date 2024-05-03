---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - projects
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.projects.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="apexName" /> | `string` |  |
| <CopyableCode code="createdAt" /> | `number` |  |
| <CopyableCode code="gitBranch" /> | `string` |  |
| <CopyableCode code="projectId" /> | `string` |  |
| <CopyableCode code="redirect" /> | `string` |  |
| <CopyableCode code="redirectStatusCode" /> | `number` |  |
| <CopyableCode code="updatedAt" /> | `number` |  |
| <CopyableCode code="verification" /> | `array` | A list of verification challenges, one of which must be completed to verify the domain for use on the project. After the challenge is complete `POST /projects/:idOrName/domains/:domain/verify` to verify the domain. Possible challenges: - If `verification.type = TXT` the `verification.domain` will be checked for a TXT record matching `verification.value`. |
| <CopyableCode code="verified" /> | `boolean` | `true` if the domain is verified for use with the project. If `false` it will not be used as an alias on this project until the challenge in `verification` is completed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_domain" /> | `SELECT` | <CopyableCode code="domain, idOrName, teamId" /> | Get project domain by project id/name and domain name. |
| <CopyableCode code="get_project_domains" /> | `SELECT` | <CopyableCode code="idOrName, teamId" /> | Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL. |
| <CopyableCode code="remove_project_domain" /> | `DELETE` | <CopyableCode code="domain, idOrName, teamId" /> | Remove a domain from a project by passing the domain name and by specifying the project by either passing the project `id` or `name` in the URL. |
| <CopyableCode code="_get_project_domains" /> | `EXEC` | <CopyableCode code="idOrName, teamId" /> | Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL. |
| <CopyableCode code="add_project_domain" /> | `EXEC` | <CopyableCode code="idOrName, teamId, data__name" /> | Add a domain to the project by passing its domain name and by specifying the project by either passing the project `id` or `name` in the URL. If the domain is not yet verified to be used on this project, the request will return `verified = false`, and the domain will need to be verified according to the `verification` challenge via `POST /projects/:idOrName/domains/:domain/verify`. If the domain already exists on the project, the request will fail with a `400` status code. |
| <CopyableCode code="update_project_domain" /> | `EXEC` | <CopyableCode code="domain, idOrName, teamId" /> | Update a project domain's configuration, including the name, git branch and redirect of the domain. |
| <CopyableCode code="verify_project_domain" /> | `EXEC` | <CopyableCode code="domain, idOrName, teamId" /> | Attempts to verify a project domain with `verified = false` by checking the correctness of the project domain's `verification` challenge. |
