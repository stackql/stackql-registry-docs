---
title: preferences
hide_title: false
hide_table_of_contents: false
keywords:
  - preferences
  - profile
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>preferences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.preferences" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="_getUserPreferences" /> | `EXEC` |  | View a list of user preferences tied to the OAuth client that generated<br />the token making the request. The user preferences endpoints allow<br />consumers of the API to store arbitrary JSON data, such as a user's font<br />size preference or preferred display name. User preferences are available<br />for each OAuth client registered to your account, and as such an account can<br />have multiple user preferences.<br /> |
| <CopyableCode code="getUserPreferences" /> | `EXEC` |  | View a list of user preferences tied to the OAuth client that generated<br />the token making the request. The user preferences endpoints allow<br />consumers of the API to store arbitrary JSON data, such as a user's font<br />size preference or preferred display name. User preferences are available<br />for each OAuth client registered to your account, and as such an account can<br />have multiple user preferences.<br /> |
| <CopyableCode code="updateUserPreferences" /> | `EXEC` |  | Updates a user's preferences. These preferences are tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user's font size preference or preferred display name. An account may have multiple preferences. Preferences, and the pertaining request body, may contain any arbitrary JSON data that the user would like to store.<br /> |
