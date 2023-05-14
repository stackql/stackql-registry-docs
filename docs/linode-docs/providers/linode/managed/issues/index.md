---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
  - managed
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.managed.issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Issue's unique ID.<br /> |
| `services` | `array` | An array of Managed Service IDs that were affected by this Issue.<br /> |
| `created` | `string` | When this Issue was created. Issues are created in response to issues detected with Managed Services, so this is also when the Issue was detected.<br /> |
| `entity` | `object` | The ticket this Managed Issue opened.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getManagedIssue` | `SELECT` | `issueId` | Returns a single Issue that is impacting or did impact one of your<br />Managed Services.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `getManagedIssues` | `SELECT` |  | Returns a paginated list of recent and ongoing issues detected on your<br />Managed Services.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedIssue` | `EXEC` | `issueId` | Returns a single Issue that is impacting or did impact one of your<br />Managed Services.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedIssues` | `EXEC` |  | Returns a paginated list of recent and ongoing issues detected on your<br />Managed Services.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
