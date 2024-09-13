---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - appengine
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

Creates, updates, deletes or gets an <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Relative name of the service within the application. Example: default.@OutputOnly |
| <CopyableCode code="name" /> | `string` | Output only. Full path to the Service resource in the API. Example: apps/myapp/services/default.@OutputOnly |
| <CopyableCode code="generatedCustomerMetadata" /> | `object` | Additional Google Generated Customer Metadata, this field won't be provided by default and can be requested by setting the IncludeExtraData field in GetServiceRequest |
| <CopyableCode code="labels" /> | `object` | A set of labels to apply to this service. Labels are key/value pairs that describe the service and all resources that belong to it (e.g., versions). The labels can be used to search and group resources, and are propagated to the usage and billing reports, enabling fine-grain analysis of costs. An example of using labels is to tag resources belonging to different environments (e.g., "env=prod", "env=qa"). Label keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, dashes, and international characters. Label keys must start with a lowercase letter or an international character. Each service can have at most 32 labels. |
| <CopyableCode code="networkSettings" /> | `object` | A NetworkSettings resource is a container for ingress settings for a version or service. |
| <CopyableCode code="split" /> | `object` | Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, servicesId" /> | Gets the current configuration of the specified service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId" /> | Lists all the services in the application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, servicesId" /> | Deletes the specified service and all enclosed versions. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId, servicesId" /> | Updates the configuration of the specified service. |

## `SELECT` examples

Lists all the services in the application.

```sql
SELECT
id,
name,
generatedCustomerMetadata,
labels,
networkSettings,
split
FROM google.appengine.services
WHERE appsId = '{{ appsId }}'; 
```

## `UPDATE` example

Updates a service only if the necessary resources are available.

```sql
UPDATE google.appengine.services
SET 
name = '{{ name }}',
id = '{{ id }}',
split = '{{ split }}',
labels = '{{ labels }}',
networkSettings = '{{ networkSettings }}',
generatedCustomerMetadata = '{{ generatedCustomerMetadata }}'
WHERE 
appsId = '{{ appsId }}'
AND servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified service resource.

```sql
DELETE FROM google.appengine.services
WHERE appsId = '{{ appsId }}'
AND servicesId = '{{ servicesId }}';
```
