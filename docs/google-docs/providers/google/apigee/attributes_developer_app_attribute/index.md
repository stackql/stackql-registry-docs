---
title: attributes_developer_app_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes_developer_app_attribute
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

Creates, updates, deletes, gets or lists a <code>attributes_developer_app_attribute</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes_developer_app_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.attributes_developer_app_attribute" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_apps_attributes_update_developer_app_attribute" /> | `UPDATE` | <CopyableCode code="appsId, attributesId, developersId, organizationsId" /> | Updates a developer app attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |

## `UPDATE` example

Updates a <code>attributes_developer_app_attribute</code> resource.

```sql
/*+ update */
UPDATE google.apigee.attributes_developer_app_attribute
SET 
value = '{{ value }}',
name = '{{ name }}'
WHERE 
appsId = '{{ appsId }}'
AND attributesId = '{{ attributesId }}'
AND developersId = '{{ developersId }}'
AND organizationsId = '{{ organizationsId }}';
```
