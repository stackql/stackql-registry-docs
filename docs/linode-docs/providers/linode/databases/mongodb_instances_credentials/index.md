---
title: mongodb_instances_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - mongodb_instances_credentials
  - databases
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
<tr><td><b>Name</b></td><td><code>mongodb_instances_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.mongodb_instances_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="password" /> | `string` | The randomly-generated root password for the Managed Database instance. |
| <CopyableCode code="username" /> | `string` | The root username for the Managed Database instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDatabasesMongoDBInstanceCredentials" /> | `SELECT` | <CopyableCode code="instanceId" /> | Display the root username and password for an accessible Managed MongoDB Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| <CopyableCode code="_getDatabasesMongoDBInstanceCredentials" /> | `EXEC` | <CopyableCode code="instanceId" /> | Display the root username and password for an accessible Managed MongoDB Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| <CopyableCode code="postDatabasesMongoDBInstanceCredentialsReset" /> | `EXEC` | <CopyableCode code="instanceId" /> | Reset the root password for a Managed MongoDB Database.<br /><br />Requires `read_write` access to the Database.<br /><br />A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/&#123;instanceId&#125;/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.<br /><br />Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.<br /><br />**Note**: Note that it may take several seconds for credentials to reset.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
