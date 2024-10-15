---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - cdn
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation} |
| <CopyableCode code="display" /> | `` | The object that represents the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | The origin of operations. |
| <CopyableCode code="properties" /> | `object` | Properties of operation, include metric specifications. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available CDN REST API operations. |
| <CopyableCode code="check_endpoint_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__name, data__type" /> | Check the availability of a resource name. This is needed for resources where name is globally unique, such as a afdx endpoint. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="data__name, data__type" /> | Check the availability of a resource name. This is needed for resources where name is globally unique, such as a CDN endpoint. |
| <CopyableCode code="check_name_availability_with_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Check the availability of a resource name. This is needed for resources where name is globally unique, such as a CDN endpoint. |
| <CopyableCode code="validate_probe" /> | `EXEC` | <CopyableCode code="subscriptionId, data__probeURL" /> | Check if the probe path is a valid path and the file can be accessed. Probe path is the path to a file hosted on the origin server to help accelerate the delivery of dynamic content via the CDN endpoint. This path is relative to the origin path specified in the endpoint configuration. |

## `SELECT` examples

Lists all of the available CDN REST API operations.


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.cdn.operations
;
```