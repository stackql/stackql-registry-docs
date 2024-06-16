---
title: db_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - db_servers
  - oracle
  - azure_isv    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_servers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, dbserverocid, resourceGroupName, subscriptionId" /> | Get a DbServer |
| <CopyableCode code="list_by_cloud_exadata_infrastructure" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | List DbServer resources by CloudExadataInfrastructure |
