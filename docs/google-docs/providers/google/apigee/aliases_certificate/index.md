---
title: aliases_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases_certificate
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

Creates, updates, deletes or gets an <code>aliases_certificate</code> resource or lists <code>aliases_certificate</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.aliases_certificate" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_keystores_aliases_get_certificate" /> | `SELECT` | <CopyableCode code="aliasesId, environmentsId, keystoresId, organizationsId" /> | Gets the certificate from an alias in PEM-encoded form. |

## `SELECT` examples

Gets the certificate from an alias in PEM-encoded form.

```sql
SELECT
contentType,
data,
extensions
FROM google.apigee.aliases_certificate
WHERE aliasesId = '{{ aliasesId }}'
AND environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
