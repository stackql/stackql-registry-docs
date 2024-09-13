---
title: registrations_importable_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_importable_domains
  - domains
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

Creates, updates, deletes or gets an <code>registrations_importable_domain</code> resource or lists <code>registrations_importable_domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_importable_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations_importable_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domains" /> | `array` | A list of domains that the calling user manages in Google Domains. |
| <CopyableCode code="nextPageToken" /> | `string` | When present, there are more results to retrieve. Set `page_token` to this value on a subsequent call to get the next page of results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_importable_domains" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) Lists domain names from [Google Domains](https://domains.google/) that can be imported to Cloud Domains using the `ImportDomain` method. Since individual users can own domains in Google Domains, the list of domains returned depends on the individual user making the call. Domains already managed by Cloud Domains are not returned. |

## `SELECT` examples

Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) Lists domain names from [Google Domains](https://domains.google/) that can be imported to Cloud Domains using the `ImportDomain` method. Since individual users can own domains in Google Domains, the list of domains returned depends on the individual user making the call. Domains already managed by Cloud Domains are not returned.

```sql
SELECT
domains,
nextPageToken
FROM google.domains.registrations_importable_domains
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
