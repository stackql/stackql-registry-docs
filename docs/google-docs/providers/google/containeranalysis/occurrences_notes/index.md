---
title: occurrences_notes
hide_title: false
hide_table_of_contents: false
keywords:
  - occurrences_notes
  - containeranalysis
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

Creates, updates, deletes or gets an <code>occurrences_note</code> resource or lists <code>occurrences_notes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>occurrences_notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.containeranalysis.occurrences_notes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. |
| <CopyableCode code="attestation" /> | `object` | Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one `Authority` for "QA" and one for "build". This note is intended to act strictly as a grouping mechanism for the attached occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the ability for a principle to attach an occurrence to a given note. It also provides a single point of lookup to find all attached attestation occurrences, even if they don't all live in the same project. |
| <CopyableCode code="build" /> | `object` | Note holding the version of the provider's builder and the signature of the provenance message in the build details occurrence. |
| <CopyableCode code="compliance" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this note was created. This field can be used as a filter in list requests. |
| <CopyableCode code="deployment" /> | `object` | An artifact that can be deployed in some runtime. |
| <CopyableCode code="discovery" /> | `object` | A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis. |
| <CopyableCode code="dsseAttestation" /> | `object` |  |
| <CopyableCode code="expirationTime" /> | `string` | Time of expiration for this note. Empty if note does not expire. |
| <CopyableCode code="image" /> | `object` | Basis describes the base image portion (Note) of the DockerImage relationship. Linked occurrences are derived from this or an equivalent image via: FROM Or an equivalent reference, e.g., a tag of the resource_url. |
| <CopyableCode code="kind" /> | `string` | Output only. The type of analysis. This field can be used as a filter in list requests. |
| <CopyableCode code="longDescription" /> | `string` | A detailed description of this note. |
| <CopyableCode code="package" /> | `object` | PackageNote represents a particular package version. |
| <CopyableCode code="relatedNoteNames" /> | `array` | Other notes related to this note. |
| <CopyableCode code="relatedUrl" /> | `array` | URLs associated with this note. |
| <CopyableCode code="sbomReference" /> | `object` | The note representing an SBOM reference. |
| <CopyableCode code="shortDescription" /> | `string` | A one sentence description of this note. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time this note was last updated. This field can be used as a filter in list requests. |
| <CopyableCode code="upgrade" /> | `object` | An Upgrade Note represents a potential upgrade of a package to a given version. For each package version combination (i.e. bash 4.0, bash 4.1, bash 4.1.2), there will be an Upgrade Note. For Windows, windows_update field represents the information related to the update. |
| <CopyableCode code="vulnerability" /> | `object` | A security vulnerability that can be found in resources. |
| <CopyableCode code="vulnerabilityAssessment" /> | `object` | A single VulnerabilityAssessmentNote represents one particular product's vulnerability assessment for one CVE. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_occurrences_get_notes" /> | `SELECT` | <CopyableCode code="locationsId, occurrencesId, projectsId" /> | Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project. |
| <CopyableCode code="projects_occurrences_get_notes" /> | `SELECT` | <CopyableCode code="occurrencesId, projectsId" /> | Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project. |

## `SELECT` examples

Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.

```sql
SELECT
name,
attestation,
build,
compliance,
createTime,
deployment,
discovery,
dsseAttestation,
expirationTime,
image,
kind,
longDescription,
package,
relatedNoteNames,
relatedUrl,
sbomReference,
shortDescription,
updateTime,
upgrade,
vulnerability,
vulnerabilityAssessment
FROM google.containeranalysis.occurrences_notes
WHERE occurrencesId = '{{ occurrencesId }}'
AND projectsId = '{{ projectsId }}'; 
```
