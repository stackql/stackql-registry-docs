---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - apps
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
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the GitHub app |
| <CopyableCode code="name" /> | `string` | The name of the GitHub app |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="client_id" /> | `string` |  |
| <CopyableCode code="client_secret" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="events" /> | `array` | The list of events for the GitHub app |
| <CopyableCode code="external_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="installations_count" /> | `integer` | The number of installations associated with the GitHub app |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="pem" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` | The set of permissions for the GitHub app |
| <CopyableCode code="slug" /> | `string` | The slug name of the GitHub app |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="webhook_secret" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_authenticated" /> | `SELECT` |  | Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the `installations_count` in the response. For more details about your app's installations, see the "[List installations for the authenticated app](https://docs.github.com/rest/apps/apps#list-installations-for-the-authenticated-app)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="get_by_slug" /> | `SELECT` | <CopyableCode code="app_slug" /> | **Note**: The `:app_slug` is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., `https://github.com/settings/apps/:app_slug`).<br /><br />If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint. |
