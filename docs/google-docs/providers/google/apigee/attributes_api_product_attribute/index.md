---
title: attributes_api_product_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes_api_product_attribute
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

Creates, updates, deletes or gets an <code>attributes_api_product_attribute</code> resource or lists <code>attributes_api_product_attribute</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes_api_product_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.attributes_api_product_attribute" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apiproducts_attributes_update_api_product_attribute" /> | `UPDATE` | <CopyableCode code="apiproductsId, attributesId, organizationsId" /> | Updates the value of an API product attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with entities also get cached for at least 180 seconds after entity is accessed during runtime. In this case, the `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |

## `UPDATE` example

Updates a attributes_api_product_attribute only if the necessary resources are available.

```sql
UPDATE google.apigee.attributes_api_product_attribute
SET 
value = '{{ value }}',
name = '{{ name }}'
WHERE 
apiproductsId = '{{ apiproductsId }}'
AND attributesId = '{{ attributesId }}'
AND organizationsId = '{{ organizationsId }}';
```
