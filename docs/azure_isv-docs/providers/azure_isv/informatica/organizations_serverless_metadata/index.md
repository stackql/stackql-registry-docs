---
title: organizations_serverless_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_serverless_metadata
  - informatica
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
<tr><td><b>Name</b></td><td><code>organizations_serverless_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.organizations_serverless_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="serverlessConfigProperties" /> | `object` | Metadata Serverless Config Properties |
| <CopyableCode code="serverlessRuntimeConfigProperties" /> | `object` | Serverless Runtime config properties. |
| <CopyableCode code="type" /> | `string` | Various types of the runtime types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
