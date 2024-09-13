
---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - prod_tt_sasportal
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

Creates, updates, deletes or gets an <code>customer</code> resource or lists <code>customers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.customers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the customer. |
| <CopyableCode code="displayName" /> | `string` | Required. Name of the organization that the customer entity represents. |
| <CopyableCode code="sasUserIds" /> | `array` | User IDs used by the devices belonging to this customer. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_get" /> | `SELECT` | <CopyableCode code="customersId" /> | Returns a requested customer. |
| <CopyableCode code="customers_list" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of requested customers. |
| <CopyableCode code="customers_patch" /> | `UPDATE` | <CopyableCode code="customersId" /> | Updates an existing customer. |
| <CopyableCode code="customers_migrate_organization" /> | `EXEC` | <CopyableCode code="" /> | Migrates a SAS organization to the cloud. This will create GCP projects for each deployment and associate them. The SAS Organization is linked to the gcp project that called the command. go/sas-legacy-customer-migration |
| <CopyableCode code="customers_provision_deployment" /> | `EXEC` | <CopyableCode code="" /> | Creates a new SAS deployment through the GCP workflow. Creates a SAS organization if an organization match is not found. |
| <CopyableCode code="customers_setup_sas_analytics" /> | `EXEC` | <CopyableCode code="" /> | Setups the a GCP Project to receive SAS Analytics messages via GCP Pub/Sub with a subscription to BigQuery. All the Pub/Sub topics and BigQuery tables are created automatically as part of this service. |

## `SELECT` examples

Returns a list of requested customers.

```sql
SELECT
name,
displayName,
sasUserIds
FROM google.prod_tt_sasportal.customers
WHERE  = '{{  }}'; 
```

## `UPDATE` example

Updates a customer only if the necessary resources are available.

```sql
UPDATE google.prod_tt_sasportal.customers
SET 
name = '{{ name }}',
sasUserIds = '{{ sasUserIds }}',
displayName = '{{ displayName }}'
WHERE 
customersId = '{{ customersId }}';
```
