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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>occurrences_notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.containeranalysis.occurrences_notes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. |
| `compliance` | `object` |  |
| `expirationTime` | `string` | Time of expiration for this note. Empty if note does not expire. |
| `attestation` | `object` | Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one `Authority` for "QA" and one for "build". This note is intended to act strictly as a grouping mechanism for the attached occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the ability for a principle to attach an occurrence to a given note. It also provides a single point of lookup to find all attached attestation occurrences, even if they don't all live in the same project. |
| `kind` | `string` | Output only. The type of analysis. This field can be used as a filter in list requests. |
| `dsseAttestation` | `object` |  |
| `longDescription` | `string` | A detailed description of this note. |
| `relatedNoteNames` | `array` | Other notes related to this note. |
| `vulnerability` | `object` | A security vulnerability that can be found in resources. |
| `package` | `object` | PackageNote represents a particular package version. |
| `sbomReference` | `object` | The note representing an SBOM reference. |
| `createTime` | `string` | Output only. The time this note was created. This field can be used as a filter in list requests. |
| `build` | `object` | Note holding the version of the provider's builder and the signature of the provenance message in the build details occurrence. |
| `deployment` | `object` | An artifact that can be deployed in some runtime. |
| `updateTime` | `string` | Output only. The time this note was last updated. This field can be used as a filter in list requests. |
| `vulnerabilityAssessment` | `object` | A single VulnerabilityAssessmentNote represents one particular product's vulnerability assessment for one CVE. |
| `upgrade` | `object` | An Upgrade Note represents a potential upgrade of a package to a given version. For each package version combination (i.e. bash 4.0, bash 4.1, bash 4.1.2), there will be an Upgrade Note. For Windows, windows_update field represents the information related to the update. |
| `image` | `object` | Basis describes the base image portion (Note) of the DockerImage relationship. Linked occurrences are derived from this or an equivalent image via: FROM Or an equivalent reference, e.g., a tag of the resource_url. |
| `shortDescription` | `string` | A one sentence description of this note. |
| `discovery` | `object` | A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis. |
| `relatedUrl` | `array` | URLs associated with this note. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_occurrences_get_notes` | `SELECT` | `occurrencesId, projectsId` |
