---
title: environments_environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_environment
  - apigee
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

Creates, updates, deletes, gets or lists a <code>environments_environment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_environment" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_update_environment" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId" /> | Updates an existing environment. When updating properties, you must pass all existing properties to the API, even if they are not being changed. If you omit properties from the payload, the properties are removed. To get the current list of properties for the environment, use the [Get Environment API](get). **Note**: Both `PUT` and `POST` methods are supported for updating an existing environment. |

## `UPDATE` example

Updates a <code>environments_environment</code> resource.

```sql
/*+ update */
UPDATE google.apigee.environments_environment
SET 
nodeConfig = '{{ nodeConfig }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
properties = '{{ properties }}',
hasAttachedFlowHooks = true|false,
apiProxyType = '{{ apiProxyType }}',
name = '{{ name }}',
deploymentType = '{{ deploymentType }}',
forwardProxyUri = '{{ forwardProxyUri }}',
type = '{{ type }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
