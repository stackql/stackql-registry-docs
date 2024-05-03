---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This authorization's ID, used for revoking access.<br /> |
| <CopyableCode code="created" /> | `string` | When this app was authorized. |
| <CopyableCode code="expiry" /> | `string` | When the app's access to your account expires. If `null`, the app's access must be revoked manually.<br /> |
| <CopyableCode code="label" /> | `string` | The name of the application you've authorized.<br /> |
| <CopyableCode code="scopes" /> | `string` | The OAuth scopes this app was authorized with.  This defines what parts of your Account the app is allowed to access.<br /> |
| <CopyableCode code="thumbnail_url" /> | `string` | The URL at which this app's thumbnail may be accessed.<br /> |
| <CopyableCode code="website" /> | `string` | The website where you can get more information about this app.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getProfileApp" /> | `SELECT` | <CopyableCode code="appId" /> | Returns information about a single app you've authorized to access your Account.<br /> |
| <CopyableCode code="getProfileApps" /> | `SELECT` |  | This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /> |
| <CopyableCode code="deleteProfileApp" /> | `DELETE` | <CopyableCode code="appId" /> | Expires this app token. This token may no longer be used to access your Account.<br /> |
| <CopyableCode code="_getProfileApp" /> | `EXEC` | <CopyableCode code="appId" /> | Returns information about a single app you've authorized to access your Account.<br /> |
| <CopyableCode code="_getProfileApps" /> | `EXEC` |  | This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /> |
