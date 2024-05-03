---
title: rollbacks
hide_title: false
hide_table_of_contents: false
keywords:
  - rollbacks
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollbacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.rollbacks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_rollback" /> | `INSERT` | <CopyableCode code="app_id" /> | Rollback an app to a previous deployment. A new deployment will be created to perform the rollback.<br />The app will be pinned to the rollback deployment preventing any new deployments from being created,<br />either manually or through Auto Deploy on Push webhooks. To resume deployments, the rollback must be<br />either committed or reverted.<br /><br />It is recommended to use the Validate App Rollback endpoint to double check if the rollback is<br />valid and if there are any warnings.<br /> |
| <CopyableCode code="commit_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Commit an app rollback. This action permanently applies the rollback and unpins the app to resume new deployments.<br /> |
| <CopyableCode code="revert_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Revert an app rollback. This action reverts the active rollback by creating a new deployment from the<br />latest app spec prior to the rollback and unpins the app to resume new deployments.<br /> |
| <CopyableCode code="validate_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Check whether an app can be rolled back to a specific deployment. This endpoint can also be used<br />to check if there are any warnings or validation conditions that will cause the rollback to proceed<br />under unideal circumstances. For example, if a component must be rebuilt as part of the rollback<br />causing it to take longer than usual.<br /> |
