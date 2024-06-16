---
title: hcrp_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - hcrp_reports
  - automanage
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
<tr><td><b>Name</b></td><td><code>hcrp_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.hcrp_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Data related to the report detail. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, machineName, reportName, resourceGroupName, subscriptionId" /> | Get information about a report associated with a configuration profile assignment run |
| <CopyableCode code="list_by_configuration_profile_assignments" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Retrieve a list of reports within a given configuration profile assignment |
