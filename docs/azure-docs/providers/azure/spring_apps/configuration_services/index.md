---
title: configuration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_services
  - spring_apps
  - azure    
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
<tr><td><b>Name</b></td><td><code>configuration_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.configuration_services" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Configuration Service and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Application Configuration Service or update the existing Application Configuration Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Application Configuration Service. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Check if the Application Configuration Service settings are valid. |
| <CopyableCode code="validate_resource" /> | `EXEC` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Check if the Application Configuration Service resource is valid. |
