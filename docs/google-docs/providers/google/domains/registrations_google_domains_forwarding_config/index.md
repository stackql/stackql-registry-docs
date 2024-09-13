---
title: registrations_google_domains_forwarding_config
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_google_domains_forwarding_config
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

Creates, updates, deletes, gets or lists a <code>registrations_google_domains_forwarding_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_google_domains_forwarding_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations_google_domains_forwarding_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domainForwardings" /> | `array` | The list of domain forwarding configurations. A forwarding configuration might not work correctly if the required DNS records are not present in the domain's authoritative DNS zone. |
| <CopyableCode code="emailForwardings" /> | `array` | The list of email forwarding configurations. A forwarding configuration might not work correctly if the required DNS records are not present in the domain's authoritative DNS zone. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrieve_google_domains_forwarding_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Lists the deprecated domain and email forwarding configurations you set up in the deprecated Google Domains UI. The configuration is present only for domains with the `google_domains_redirects_data_available` set to `true` in the `Registration`'s `dns_settings`. A forwarding configuration might not work correctly if required DNS records are not present in the domain's authoritative DNS Zone. |

## `SELECT` examples

Lists the deprecated domain and email forwarding configurations you set up in the deprecated Google Domains UI. The configuration is present only for domains with the `google_domains_redirects_data_available` set to `true` in the `Registration`'s `dns_settings`. A forwarding configuration might not work correctly if required DNS records are not present in the domain's authoritative DNS Zone.

```sql
SELECT
domainForwardings,
emailForwardings
FROM google.domains.registrations_google_domains_forwarding_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND registrationsId = '{{ registrationsId }}'; 
```
