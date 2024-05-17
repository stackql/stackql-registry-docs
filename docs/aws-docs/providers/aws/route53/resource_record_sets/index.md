---
title: resource_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_record_sets
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Resource Record Sets in a Hosted Zone

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Record Sets in a Hosted Zone</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.resource_record_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Hosted Zone</td></tr>
<tr><td><CopyableCode code="alias_target" /></td><td><code>object</code></td><td>Alias resource record sets only: Information about the Amazon Web Services resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.</td></tr>
<tr><td><CopyableCode code="cidr_routing_config" /></td><td><code>object</code></td><td>The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.</td></tr>
<tr><td><CopyableCode code="failover" /></td><td><code>string</code></td><td>Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover; for the other resource record set, you specify SECONDARY. In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set. Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets: When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set. When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. You can't create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets. For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true. For more information about configuring failover for Route 53, see the following topics in the Amazon Route 53 Developer Guide: Route 53 Health Checks and DNS Failover Configuring Failover in a Private Hosted Zone</td></tr>
<tr><td><CopyableCode code="geo_location" /></td><td><code>object</code></td><td>A complex type that contains information about a geographic location.</td></tr>
<tr><td><CopyableCode code="health_check_id" /></td><td><code>string</code></td><td>If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the HealthCheckId element and specify the ID of the applicable health check. Route 53 determines whether a resource record set is healthy based on one of the following: By periodically sending a request to the endpoint that is specified in the health check By aggregating the status of a specified group of health checks (calculated health checks) By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check. For more information, see the following topics in the Amazon Route 53 Developer Guide: How Amazon Route 53 Determines Whether an Endpoint Is Healthy Route 53 Health Checks and DNS Failover Configuring Failover in a Private Hosted Zone When to Specify HealthCheckId Specifying a value for HealthCheckId is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations: Non-alias resource record sets: You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets. If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly. Alias resource record sets: You specify the following settings: You set EvaluateTargetHealth to true for an alias resource record set in a group of resource record sets that have the same routing policy</td></tr>
<tr><td><CopyableCode code="multi_value_answer" /></td><td><code>boolean</code></td><td>Multivalue answer resource record sets only: To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify true for MultiValueAnswer. Note the following: If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy. Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records. If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records. When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records. If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. You can't create multivalue answer alias records.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>For ChangeResourceRecordSets requests, the name of the record that you want to create, update, or delete. For ListResourceRecordSets responses, the name of a record in the specified hosted zone. ChangeResourceRecordSets Only Enter a fully qualified domain name, for example, www.example.com. You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical. For information about how to specify characters other than a-z, 0-9, and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide. You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, *.example.com. Note the following: The * must replace the entire label. For example, you can't specify *prod.example.com or prod*.example.com. The * can't replace any of the middle labels, for example, marketing.*.example.com. If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. You can't use the * wildcard for resource records sets that have a type of NS.</td></tr>
<tr><td><CopyableCode code="resource_records" /></td><td><code>array</code></td><td>Information about the resource records to act upon.</td></tr>
<tr><td><CopyableCode code="set_identifier" /></td><td><code>string</code></td><td>An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of SetIdentifier must be unique for each resource record set that has the same combination of DNS name and type. Omit SetIdentifier for any other resource record set that has the same combination of DNS name and type. You can't use SetIdentifier to differentiate among resource record sets that have the same DNS name and type.</td></tr>
<tr><td><CopyableCode code="ttl" /></td><td><code>integer</code></td><td>The resource record cache time to live (TTL), in seconds. Note the following: If you're creating an alias resource record set, omit TTL. Amazon Route 53 uses the TTL for the alias target. If you're associating this resource record set with a health check (if you're adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status. All of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets must have the same value for TTL.</td></tr>
<tr><td><CopyableCode code="traffic_policy_instance_id" /></td><td><code>string</code></td><td>When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Route 53 created this resource record set for.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide.</td></tr>
<tr><td><CopyableCode code="weight" /></td><td><code>integer</code></td><td>If you want to create a weighted resource record set, an alias resource record set, or a latency resource record set and specify weighted routing, specify a value between 0 and 255. You can't specify this value for other types of resource record sets. For weighted resource record sets, Route 53 uses the value to determine how often the response is served from this resource record set compared to other resource record sets in the same group. For example, suppose the following weighted resource record sets are configured for a domain, and the domain contains a CNAME record: example.com A</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
alias_target,
cidr_routing_config,
failover,
geo_location,
health_check_id,
multi_value_answer,
name,
resource_records,
set_identifier,
ttl,
traffic_policy_instance_id,
type,
weight
FROM aws.route53.resource_record_sets
WHERE Id = '<HOSTEDZONEID>';
```





