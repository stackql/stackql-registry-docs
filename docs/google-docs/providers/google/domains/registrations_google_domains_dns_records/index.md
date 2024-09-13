
---
title: registrations_google_domains_dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_google_domains_dns_records
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

Creates, updates, deletes or gets an <code>registrations_google_domains_dns_record</code> resource or lists <code>registrations_google_domains_dns_records</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_google_domains_dns_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations_google_domains_dns_records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | When present, there are more results to retrieve. Set `page_token` to this value on a subsequent call to get the next page of results. |
| <CopyableCode code="rrset" /> | `array` | The resource record set resources (DNS Zone records). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_google_domains_dns_records" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Lists the DNS records from the Google Domains DNS zone for domains that use the deprecated `google_domains_dns` in the `Registration`'s `dns_settings`. |

## `SELECT` examples

Lists the DNS records from the Google Domains DNS zone for domains that use the deprecated `google_domains_dns` in the `Registration`'s `dns_settings`.

```sql
SELECT
nextPageToken,
rrset
FROM google.domains.registrations_google_domains_dns_records
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND registrationsId = '{{ registrationsId }}'; 
```
