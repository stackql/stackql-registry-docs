
---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
  - compute
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

Creates, updates, deletes or gets an <code>forwarding_rule</code> resource or lists <code>forwarding_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.forwarding_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. For Private Service Connect forwarding rules that forward traffic to Google APIs, the forwarding rule name must be a 1-20 characters string with lowercase letters and numbers and must start with a letter. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="IPAddress" /> | `string` | IP address for which this forwarding rule accepts traffic. When a client sends traffic to this IP address, the forwarding rule directs the traffic to the referenced target or backendService. While creating a forwarding rule, specifying an IPAddress is required under the following circumstances: - When the target is set to targetGrpcProxy and validateForProxyless is set to true, the IPAddress should be set to 0.0.0.0. - When the target is a Private Service Connect Google APIs bundle, you must specify an IPAddress. Otherwise, you can optionally specify an IP address that references an existing static (reserved) IP address resource. When omitted, Google Cloud assigns an ephemeral IP address. Use one of the following formats to specify an IP address while creating a forwarding rule: * IP address number, as in `100.1.2.3` * IPv6 address range, as in `2600:1234::/96` * Full resource URL, as in https://www.googleapis.com/compute/v1/projects/ project_id/regions/region/addresses/address-name * Partial URL or by name, as in: - projects/project_id/regions/region/addresses/address-name - regions/region/addresses/address-name - global/addresses/address-name - address-name The forwarding rule's target or backendService, and in most cases, also the loadBalancingScheme, determine the type of IP address that you can use. For detailed information, see [IP address specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications). When reading an IPAddress, the API always returns the IP address number. |
| <CopyableCode code="IPProtocol" /> | `string` | The IP protocol to which this rule applies. For protocol forwarding, valid options are TCP, UDP, ESP, AH, SCTP, ICMP and L3_DEFAULT. The valid IP protocols are different for different load balancing products as described in [Load balancing features](https://cloud.google.com/load-balancing/docs/features#protocols_from_the_load_balancer_to_the_backends). |
| <CopyableCode code="allPorts" /> | `boolean` | The ports, portRange, and allPorts fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule. The allPorts field has the following limitations: - It requires that the forwarding rule IPProtocol be TCP, UDP, SCTP, or L3_DEFAULT. - It's applicable only to the following products: internal passthrough Network Load Balancers, backend service-based external passthrough Network Load Balancers, and internal and external protocol forwarding. - Set this field to true to allow packets addressed to any port or packets lacking destination port information (for example, UDP fragments after the first fragment) to be forwarded to the backends configured with this forwarding rule. The L3_DEFAULT protocol requires allPorts be set to true.  |
| <CopyableCode code="allowGlobalAccess" /> | `boolean` | If set to true, clients can access the internal passthrough Network Load Balancers, the regional internal Application Load Balancer, and the regional internal proxy Network Load Balancer from all regions. If false, only allows access from the local region the load balancer is located at. Note that for INTERNAL_MANAGED forwarding rules, this field cannot be changed after the forwarding rule is created. |
| <CopyableCode code="allowPscGlobalAccess" /> | `boolean` | This is used in PSC consumer ForwardingRule to control whether the PSC endpoint can be accessed from another region. |
| <CopyableCode code="backendService" /> | `string` | Identifies the backend service to which the forwarding rule sends traffic. Required for internal and external passthrough Network Load Balancers; must be omitted for all other load balancer types. |
| <CopyableCode code="baseForwardingRule" /> | `string` | [Output Only] The URL for the corresponding base forwarding rule. By base forwarding rule, we mean the forwarding rule that has the same IP address, protocol, and port settings with the current forwarding rule, but without sourceIPRanges specified. Always empty if the current forwarding rule does not have sourceIPRanges specified. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a ForwardingRule. Include the fingerprint in patch request to ensure that you do not overwrite changes that were applied from another concurrent request. To see the latest fingerprint, make a get() request to retrieve a ForwardingRule. |
| <CopyableCode code="ipCollection" /> | `string` | Resource reference of a PublicDelegatedPrefix. The PDP must be a sub-PDP in EXTERNAL_IPV6_FORWARDING_RULE_CREATION mode. Use one of the following formats to specify a sub-PDP when creating an IPv6 NetLB forwarding rule using BYOIP: Full resource URL, as in https://www.googleapis.com/compute/v1/projects/project_id/regions/region /publicDelegatedPrefixes/sub-pdp-name Partial URL, as in: - projects/project_id/regions/region/publicDelegatedPrefixes/sub-pdp-name - regions/region/publicDelegatedPrefixes/sub-pdp-name  |
| <CopyableCode code="ipVersion" /> | `string` | The IP Version that will be used by this forwarding rule. Valid options are IPV4 or IPV6. |
| <CopyableCode code="isMirroringCollector" /> | `boolean` | Indicates whether or not this load balancer can be used as a collector for packet mirroring. To prevent mirroring loops, instances behind this load balancer will not have their traffic mirrored even if a PacketMirroring rule applies to them. This can only be set to true for load balancers that have their loadBalancingScheme set to INTERNAL. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#forwardingRule for forwarding rule resources. |
| <CopyableCode code="labelFingerprint" /> | `string` | A fingerprint for the labels being applied to this resource, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a ForwardingRule. |
| <CopyableCode code="labels" /> | `object` | Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty. |
| <CopyableCode code="loadBalancingScheme" /> | `string` | Specifies the forwarding rule type. For more information about forwarding rules, refer to Forwarding rule concepts. |
| <CopyableCode code="metadataFilters" /> | `array` | Opaque filter criteria used by load balancer to restrict routing configuration to a limited set of xDS compliant clients. In their xDS requests to load balancer, xDS clients present node metadata. When there is a match, the relevant configuration is made available to those proxies. Otherwise, all the resources (e.g. TargetHttpProxy, UrlMap) referenced by the ForwardingRule are not visible to those proxies. For each metadataFilter in this list, if its filterMatchCriteria is set to MATCH_ANY, at least one of the filterLabels must match the corresponding label provided in the metadata. If its filterMatchCriteria is set to MATCH_ALL, then all of its filterLabels must match with corresponding labels provided in the metadata. If multiple metadataFilters are specified, all of them need to be satisfied in order to be considered a match. metadataFilters specified here will be applifed before those specified in the UrlMap that this ForwardingRule references. metadataFilters only applies to Loadbalancers that have their loadBalancingScheme set to INTERNAL_SELF_MANAGED. |
| <CopyableCode code="network" /> | `string` | This field is not used for global external load balancing. For internal passthrough Network Load Balancers, this field identifies the network that the load balanced IP should belong to for this forwarding rule. If the subnetwork is specified, the network of the subnetwork will be used. If neither subnetwork nor this field is specified, the default network will be used. For Private Service Connect forwarding rules that forward traffic to Google APIs, a network must be provided. |
| <CopyableCode code="networkTier" /> | `string` | This signifies the networking tier used for configuring this load balancer and can only take the following values: PREMIUM, STANDARD. For regional ForwardingRule, the valid values are PREMIUM and STANDARD. For GlobalForwardingRule, the valid value is PREMIUM. If this field is not specified, it is assumed to be PREMIUM. If IPAddress is specified, this value must be equal to the networkTier of the Address. |
| <CopyableCode code="noAutomateDnsZone" /> | `boolean` | This is used in PSC consumer ForwardingRule to control whether it should try to auto-generate a DNS zone or not. Non-PSC forwarding rules do not use this field. Once set, this field is not mutable. |
| <CopyableCode code="portRange" /> | `string` | The ports, portRange, and allPorts fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule. The portRange field has the following limitations: - It requires that the forwarding rule IPProtocol be TCP, UDP, or SCTP, and - It's applicable only to the following products: external passthrough Network Load Balancers, internal and external proxy Network Load Balancers, internal and external Application Load Balancers, external protocol forwarding, and Classic VPN. - Some products have restrictions on what ports can be used. See port specifications for details. For external forwarding rules, two or more forwarding rules cannot use the same [IPAddress, IPProtocol] pair, and cannot have overlapping portRanges. For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same [IPAddress, IPProtocol] pair, and cannot have overlapping portRanges. @pattern: \\d+(?:-\\d+)? |
| <CopyableCode code="ports" /> | `array` | The ports, portRange, and allPorts fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule. The ports field has the following limitations: - It requires that the forwarding rule IPProtocol be TCP, UDP, or SCTP, and - It's applicable only to the following products: internal passthrough Network Load Balancers, backend service-based external passthrough Network Load Balancers, and internal protocol forwarding. - You can specify a list of up to five ports by number, separated by commas. The ports can be contiguous or discontiguous. For external forwarding rules, two or more forwarding rules cannot use the same [IPAddress, IPProtocol] pair if they share at least one port number. For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same [IPAddress, IPProtocol] pair if they share at least one port number. @pattern: \\d+(?:-\\d+)? |
| <CopyableCode code="pscConnectionId" /> | `string` | [Output Only] The PSC connection id of the PSC forwarding rule. |
| <CopyableCode code="pscConnectionStatus" /> | `string` |  |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional forwarding rule resides. This field is not applicable to global forwarding rules. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="serviceDirectoryRegistrations" /> | `array` | Service Directory resources to register this forwarding rule with. Currently, only supports a single Service Directory resource. |
| <CopyableCode code="serviceLabel" /> | `string` | An optional prefix to the service name for this forwarding rule. If specified, the prefix is the first label of the fully qualified service name. The label must be 1-63 characters long, and comply with RFC1035. Specifically, the label must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is only used for internal load balancing. |
| <CopyableCode code="serviceName" /> | `string` | [Output Only] The internal fully qualified service name for this forwarding rule. This field is only used for internal load balancing. |
| <CopyableCode code="sourceIpRanges" /> | `array` | If not empty, this forwarding rule will only forward the traffic when the source IP address matches one of the IP addresses or CIDR ranges set here. Note that a forwarding rule can only have up to 64 source IP ranges, and this field can only be used with a regional forwarding rule whose scheme is EXTERNAL. Each source_ip_range entry should be either an IP address (for example, 1.2.3.4) or a CIDR range (for example, 1.2.3.0/24). |
| <CopyableCode code="subnetwork" /> | `string` | This field identifies the subnetwork that the load balanced IP should belong to for this forwarding rule, used with internal load balancers and external passthrough Network Load Balancers with IPv6. If the network specified is in auto subnet mode, this field is optional. However, a subnetwork must be specified if the network is in custom subnet mode or when creating external forwarding rule with IPv6. |
| <CopyableCode code="target" /> | `string` | The URL of the target resource to receive the matched traffic. For regional forwarding rules, this target must be in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource. The forwarded traffic must be of a type appropriate to the target object. - For load balancers, see the "Target" column in [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications). - For Private Service Connect forwarding rules that forward traffic to Google APIs, provide the name of a supported Google API bundle: - vpc-sc - APIs that support VPC Service Controls. - all-apis - All supported Google APIs. - For Private Service Connect forwarding rules that forward traffic to managed services, the target must be a service attachment. The target is not mutable once set as a service attachment.  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of forwarding rules. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="forwardingRule, project, region" /> | Returns the specified ForwardingRule resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of ForwardingRule resources available to the specified project and region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a ForwardingRule resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="forwardingRule, project, region" /> | Deletes the specified ForwardingRule resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="forwardingRule, project, region" /> | Updates the specified forwarding rule with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. Currently, you can only patch the network_tier field. |
| <CopyableCode code="set_labels" /> | `EXEC` | <CopyableCode code="project, region, resource" /> | Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation. |
| <CopyableCode code="set_target" /> | `EXEC` | <CopyableCode code="forwardingRule, project, region" /> | Changes target URL for forwarding rule. The new target should be of the same type as the old target. |

## `SELECT` examples

Retrieves an aggregated list of forwarding rules. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
IPAddress,
IPProtocol,
allPorts,
allowGlobalAccess,
allowPscGlobalAccess,
backendService,
baseForwardingRule,
creationTimestamp,
fingerprint,
ipCollection,
ipVersion,
isMirroringCollector,
kind,
labelFingerprint,
labels,
loadBalancingScheme,
metadataFilters,
network,
networkTier,
noAutomateDnsZone,
portRange,
ports,
pscConnectionId,
pscConnectionStatus,
region,
selfLink,
serviceDirectoryRegistrations,
serviceLabel,
serviceName,
sourceIpRanges,
subnetwork,
target
FROM google.compute.forwarding_rules
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>forwarding_rules</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.forwarding_rules (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
region,
IPAddress,
IPProtocol,
portRange,
ports,
target,
selfLink,
loadBalancingScheme,
subnetwork,
network,
backendService,
serviceDirectoryRegistrations,
serviceLabel,
serviceName,
networkTier,
labels,
labelFingerprint,
ipVersion,
fingerprint,
allPorts,
allowGlobalAccess,
metadataFilters,
isMirroringCollector,
sourceIpRanges,
pscConnectionId,
pscConnectionStatus,
baseForwardingRule,
allowPscGlobalAccess,
noAutomateDnsZone,
ipCollection
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ IPAddress }}',
'{{ IPProtocol }}',
'{{ portRange }}',
'{{ ports }}',
'{{ target }}',
'{{ selfLink }}',
'{{ loadBalancingScheme }}',
'{{ subnetwork }}',
'{{ network }}',
'{{ backendService }}',
'{{ serviceDirectoryRegistrations }}',
'{{ serviceLabel }}',
'{{ serviceName }}',
'{{ networkTier }}',
'{{ labels }}',
'{{ labelFingerprint }}',
'{{ ipVersion }}',
'{{ fingerprint }}',
true|false,
true|false,
'{{ metadataFilters }}',
true|false,
'{{ sourceIpRanges }}',
'{{ pscConnectionId }}',
'{{ pscConnectionStatus }}',
'{{ baseForwardingRule }}',
true|false,
true|false,
'{{ ipCollection }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: region
        value: '{{ region }}'
      - name: IPAddress
        value: '{{ IPAddress }}'
      - name: IPProtocol
        value: '{{ IPProtocol }}'
      - name: portRange
        value: '{{ portRange }}'
      - name: ports
        value: '{{ ports }}'
      - name: target
        value: '{{ target }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: loadBalancingScheme
        value: '{{ loadBalancingScheme }}'
      - name: subnetwork
        value: '{{ subnetwork }}'
      - name: network
        value: '{{ network }}'
      - name: backendService
        value: '{{ backendService }}'
      - name: serviceDirectoryRegistrations
        value: '{{ serviceDirectoryRegistrations }}'
      - name: serviceLabel
        value: '{{ serviceLabel }}'
      - name: serviceName
        value: '{{ serviceName }}'
      - name: networkTier
        value: '{{ networkTier }}'
      - name: labels
        value: '{{ labels }}'
      - name: labelFingerprint
        value: '{{ labelFingerprint }}'
      - name: ipVersion
        value: '{{ ipVersion }}'
      - name: fingerprint
        value: '{{ fingerprint }}'
      - name: allPorts
        value: '{{ allPorts }}'
      - name: allowGlobalAccess
        value: '{{ allowGlobalAccess }}'
      - name: metadataFilters
        value: '{{ metadataFilters }}'
      - name: isMirroringCollector
        value: '{{ isMirroringCollector }}'
      - name: sourceIpRanges
        value: '{{ sourceIpRanges }}'
      - name: pscConnectionId
        value: '{{ pscConnectionId }}'
      - name: pscConnectionStatus
        value: '{{ pscConnectionStatus }}'
      - name: baseForwardingRule
        value: '{{ baseForwardingRule }}'
      - name: allowPscGlobalAccess
        value: '{{ allowPscGlobalAccess }}'
      - name: noAutomateDnsZone
        value: '{{ noAutomateDnsZone }}'
      - name: ipCollection
        value: '{{ ipCollection }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a forwarding_rule only if the necessary resources are available.

```sql
UPDATE google.compute.forwarding_rules
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
IPAddress = '{{ IPAddress }}',
IPProtocol = '{{ IPProtocol }}',
portRange = '{{ portRange }}',
ports = '{{ ports }}',
target = '{{ target }}',
selfLink = '{{ selfLink }}',
loadBalancingScheme = '{{ loadBalancingScheme }}',
subnetwork = '{{ subnetwork }}',
network = '{{ network }}',
backendService = '{{ backendService }}',
serviceDirectoryRegistrations = '{{ serviceDirectoryRegistrations }}',
serviceLabel = '{{ serviceLabel }}',
serviceName = '{{ serviceName }}',
networkTier = '{{ networkTier }}',
labels = '{{ labels }}',
labelFingerprint = '{{ labelFingerprint }}',
ipVersion = '{{ ipVersion }}',
fingerprint = '{{ fingerprint }}',
allPorts = true|false,
allowGlobalAccess = true|false,
metadataFilters = '{{ metadataFilters }}',
isMirroringCollector = true|false,
sourceIpRanges = '{{ sourceIpRanges }}',
pscConnectionId = '{{ pscConnectionId }}',
pscConnectionStatus = '{{ pscConnectionStatus }}',
baseForwardingRule = '{{ baseForwardingRule }}',
allowPscGlobalAccess = true|false,
noAutomateDnsZone = true|false,
ipCollection = '{{ ipCollection }}'
WHERE 
forwardingRule = '{{ forwardingRule }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified forwarding_rule resource.

```sql
DELETE FROM google.compute.forwarding_rules
WHERE forwardingRule = '{{ forwardingRule }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
