---
title: serverless_runtimes_by_informatica_organization_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_runtimes_by_informatica_organization_resources
  - informatica
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

Creates, updates, deletes, gets or lists a <code>serverless_runtimes_by_informatica_organization_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_runtimes_by_informatica_organization_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.serverless_runtimes_by_informatica_organization_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Serverless Runtime properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | List InformaticaServerlessRuntimeResource resources by InformaticaOrganizationResource |

## `SELECT` examples

List InformaticaServerlessRuntimeResource resources by InformaticaOrganizationResource


```sql
SELECT
properties
FROM azure_isv.informatica.serverless_runtimes_by_informatica_organization_resources
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```